using System;
using System.Collections.Generic;
using System.Globalization;
using UnityEngine;

// Supplementary example. Virtual replay only, not a physical controller.
public class JointStateReplay : MonoBehaviour
{
    [Serializable]
    public class Joint
    {
        public Transform target;
        public Vector3 localAxis = Vector3.up;
        public bool revolute;
        public float min;
        public float max;
        [NonSerialized] public Vector3 origin;
        [NonSerialized] public Quaternion rotation;
    }
    public Joint[] joints = new Joint[4];
    public TextAsset jointCsv;
    public float metresToUnityUnits = 1f;
    private readonly List<float[]> samples = new List<float[]>();
    private float elapsed;
    private int index;

    private void Start()
    {
        if (joints == null || joints.Length != 4 || jointCsv == null ||
            metresToUnityUnits <= 0)
        { Fail("Configure four joints, scale and a CSV."); return; }
        for (int i = 0; i < 4; i++)
        {
            Joint j = joints[i];
            if (j == null || j.target == null || j.localAxis.sqrMagnitude < 0.00001f ||
                j.min >= j.max || j.revolute != (i == 0 || i == 3))
            { Fail("Invalid R-P-P-R joint configuration."); return; }
            j.origin = j.target.localPosition;
            j.rotation = j.target.localRotation;
        }
        string[] lines = jointCsv.text.Split(new[] { '\r', '\n' },
            StringSplitOptions.RemoveEmptyEntries);
        if (lines.Length < 2 || lines[0].Trim() != "time_s,q1_rad,q2_m,q3_m,q4_rad")
        { Fail("Expected joint-state CSV header and samples."); return; }
        for (int i = 1; i < lines.Length; i++)
        {
            string[] cells = lines[i].Split(',');
            if (cells.Length != 5) { Fail("Invalid CSV column count."); return; }
            float[] s = new float[5];
            for (int k = 0; k < 5; k++)
                if (!float.TryParse(cells[k], NumberStyles.Float, CultureInfo.InvariantCulture,
                    out s[k]) || float.IsNaN(s[k]) || float.IsInfinity(s[k]))
                { Fail("Invalid numeric sample."); return; }
            if ((samples.Count == 0 && s[0] != 0f) ||
                (samples.Count > 0 && s[0] <= samples[samples.Count - 1][0]))
            { Fail("Timestamps must start at zero and increase."); return; }
            samples.Add(s);
        }
        Apply(samples[0], samples[0], 0);
    }
    private void Update()
    {
        if (samples.Count == 0) return;
        elapsed += Time.deltaTime;
        while (index + 1 < samples.Count && samples[index + 1][0] <= elapsed)
            index++;
        int next = Math.Min(index + 1, samples.Count - 1);
        float alpha = next == index ? 0f :
            Mathf.InverseLerp(samples[index][0], samples[next][0], elapsed);
        Apply(samples[index], samples[next], alpha);
        if (next == index) enabled = false;
    }
    private void Apply(float[] a, float[] b, float alpha)
    {
        for (int i = 0; i < joints.Length; i++)
        {
            Joint j = joints[i];
            float q = Mathf.Clamp(Mathf.Lerp(a[i + 1], b[i + 1], alpha), j.min, j.max);
            Vector3 axis = j.localAxis.normalized;
            if (j.revolute)
                j.target.localRotation = j.rotation * Quaternion.AngleAxis(q * Mathf.Rad2Deg, axis);
            else
                j.target.localPosition = j.origin + j.rotation * axis * q * metresToUnityUnits;
        }
    }
    private void Fail(string message)
    {
        Debug.LogError(message, this);
        enabled = false;
    }
}
